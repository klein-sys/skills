# Pull Request (PR) Template & Checklist

## PR Description Template

```markdown
### Description
[Concise summary of what this change accomplishes and why it is needed.]

### Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Refactoring or documentation update

### Key Architectural / Implementation Decisions
- Decision 1: ...
- Decision 2: ...

### How Has This Been Tested?
- [ ] Unit tests added / updated: `pytest tests/test_auth.py`
- [ ] Integration tests executed locally: `npm run test:e2e`
- [ ] Manual verification steps followed below:
  1. Navigate to `/login`
  2. Enter test credentials `alice@example.com`
  3. Verify redirected to dashboard with valid session cookie

### Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented complex or non-obvious code sections
- [ ] I have updated corresponding documentation
- [ ] No new compiler or linter warnings are generated
- [ ] My changes do not expose credentials, secrets, or internal hostnames
```
