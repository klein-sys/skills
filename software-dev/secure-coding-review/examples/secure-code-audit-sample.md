# Real-World Secure Code Audit Sample

### Scenario: Auditing a Profile Update & Avatar Endpoint

#### Vulnerable Code:
```python
@app.post("/api/user/{user_id}/avatar")
def update_avatar(user_id: int, file: UploadFile = File(...)):
    # Vulnerability 1: Insecure Direct Object Reference (IDOR)
    # No check whether current authenticated caller == user_id
    
    # Vulnerability 2: Path Traversal
    filename = file.filename
    dest_path = f"/var/www/uploads/{filename}"
    with open(dest_path, "wb") as f:
        f.write(file.file.read())
        
    return {"status": "ok", "url": dest_path}
```

---

#### Security Audit Findings & Remediations:

1. **Finding 1: High - IDOR (Insecure Direct Object Reference)**
   - *Risk*: Any logged-in user can overwrite any other user's avatar or profile by tampering with the `{user_id}` route parameter.
   - *Fix*: Extract user identity strictly from the verified session/JWT token rather than an untrusted URL parameter.

2. **Finding 2: Critical - Arbitrary File Write / Path Traversal**
   - *Risk*: Attacker sends `../../../../etc/cron.d/evil` as `file.filename`, leading to Remote Code Execution (RCE).
   - *Fix*: Generate a secure UUID filename on the server. Never use client-supplied file names directly. Validate MIME type and file magic bytes.

#### Hardened Code:
```python
import uuid
import pathlib
from fastapi import APIRouter, Depends, HTTPException, UploadFile, status

router = APIRouter()
ALLOWED_MIME_TYPES = {"image/png", "image/jpeg", "image/webp"}
UPLOAD_DIR = pathlib.Path("/var/app/safe_uploads").resolve()

@router.post("/api/user/avatar")
def update_avatar(
    file: UploadFile,
    current_user: User = Depends(get_current_authenticated_user)
):
    # Verify Content-Type
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid image format. Allowed: PNG, JPEG, WEBP."
        )

    # Secure random UUID name with safe extension
    ext = ".png" if file.content_type == "image/png" else ".jpg"
    safe_filename = f"{uuid.uuid4().hex}{ext}"
    dest_path = (UPLOAD_DIR / safe_filename).resolve()

    # Ensure path cannot escape UPLOAD_DIR
    if not dest_path.is_relative_to(UPLOAD_DIR):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid path")

    with open(dest_path, "wb") as buffer:
        buffer.write(file.file.read())

    # Update database scoping to authenticated user
    current_user.avatar_filename = safe_filename
    db.commit()

    return {"status": "success", "avatar_id": safe_filename}
```
