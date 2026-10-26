# Accessible Component Patterns

## 1. Accessible Form Field with Error Messaging

```html
<div class="form-group">
  <label for="user-email" class="form-label">
    Email Address <span aria-hidden="true">*</span>
  </label>
  <input
    type="email"
    id="user-email"
    name="email"
    class="form-input"
    required
    aria-required="true"
    aria-invalid="true"
    aria-describedby="email-hint email-error"
  />
  <p id="email-hint" class="form-hint">We'll never share your email.</p>
  <p id="email-error" class="form-error" role="alert">Please enter a valid email address.</p>
</div>
```

---

## 2. Accessible Modal Dialog with Focus Trap

```html
<button id="open-btn" aria-haspopup="dialog" aria-controls="modal-dialog">
  Edit Profile
</button>

<div
  id="modal-dialog"
  role="dialog"
  aria-modal="true"
  aria-labelledby="dialog-title"
  aria-describedby="dialog-desc"
  hidden
>
  <div class="modal-backdrop"></div>
  <div class="modal-content">
    <h2 id="dialog-title">Edit Profile Information</h2>
    <p id="dialog-desc">Update your display name and public contact email.</p>

    <form id="profile-form">
      <label for="name">Name</label>
      <input type="text" id="name" />
      
      <div class="modal-actions">
        <button type="button" id="cancel-btn">Cancel</button>
        <button type="submit" id="save-btn">Save Changes</button>
      </div>
    </form>
  </div>
</div>
```

### Essential JavaScript Behavior:
1. When opening: Save reference to `#open-btn`, remove `hidden`, set focus to the first interactive element inside (`#name`).
2. On `keydown`:
   - If `Escape` key pressed: close modal and focus back to `#open-btn`.
   - If `Tab` key pressed: wrap focus from `#save-btn` back to `#cancel-btn` (focus trapping).
