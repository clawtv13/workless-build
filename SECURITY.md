# Security Guidelines

## 🔒 MANDATORY: Never Hardcode Secrets

**NEVER commit these to Git:**
- ❌ API keys (OpenAI, Anthropic, Google, etc.)
- ❌ Database passwords
- ❌ GitHub tokens
- ❌ OAuth secrets
- ❌ Private keys
- ❌ Email credentials

**ALWAYS use environment variables:**
```python
import os
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY not found in environment")
```

## ✅ Correct Pattern

**1. Create `.env` file (git-ignored):**
```bash
# .env (NEVER commit this)
GEMINI_API_KEY=your_actual_key_here
OPENAI_API_KEY=sk-xxx
```

**2. Load in code:**
```python
import os
from dotenv import load_dotenv

load_dotenv()  # Loads .env file
API_KEY = os.getenv("API_KEY")
```

**3. Provide `.env.example` (safe to commit):**
```bash
# .env.example
API_KEY=your_key_here
DATABASE_URL=postgres://...
```

## 🚨 What Happens When You Leak

**GitHub bots detect secrets within minutes:**
1. Secret committed → pushed to public repo
2. GitHub Secret Scanning detects pattern
3. GitHub notifies provider (Google, OpenAI, etc.)
4. Provider **revokes key immediately**
5. Your app breaks in production

**Real example (today):**
- Gemini API key hardcoded in `scripts/generate_image_final.py`
- Committed to public repo
- Detected and revoked within hours
- Had to generate new key + fix all scripts

## 🛡️ Prevention Checklist

Before committing:

- [ ] No API keys in code
- [ ] No passwords in config files
- [ ] `.env` in `.gitignore`
- [ ] `.env.example` provided (with fake values)
- [ ] All scripts check `os.getenv()` and fail gracefully if missing

## 🔍 Audit Command

Check for leaked secrets:
```bash
# From project root
grep -r "AIza\|sk-\|ghp_\|api[_-]key.*=.*['\"]" . \
  --exclude-dir=node_modules \
  --exclude-dir=venv \
  --exclude-dir=.git \
  --include="*.py" \
  --include="*.js" \
  --include="*.ts"
```

Should return ZERO results (or only `.env.example` with placeholders).

## 🚑 If You Already Leaked

1. **Revoke compromised key immediately** (provider dashboard)
2. **Generate new key**
3. **Update `.env` file** (local, never commit)
4. **Fix code** to use `os.getenv()`
5. **Optional:** Remove from Git history:
   ```bash
   git filter-branch --force --index-filter \
     "git rm --cached --ignore-unmatch path/to/file" \
     --prune-empty --tag-name-filter cat -- --all
   ```
6. **Force push** (only if repo is yours alone)

## 📚 References

- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)
- [OWASP API Security](https://owasp.org/www-project-api-security/)
- [Python dotenv](https://pypi.org/project/python-dotenv/)

---

**Remember:** If it's sensitive, it goes in `.env`. Period.
