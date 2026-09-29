# Keeping local credentials private

Keep Google Cloud service-account JSON credentials outside the repository, or in
the ignored `secrets/` directory. A configured local copy must point its existing
`credential_path` to that private file. The current loader explicitly reads a JSON
file; adding an environment variable alone does not change that behavior.

Keep image inputs and OCR output private unless they are intentional, sanitized
public examples. Do not commit real keys or provider-dashboard screenshots with
visible credentials. Use inert placeholders in documentation.

Ignore rules prevent new untracked files from being added accidentally; they do
not remove already tracked files or earlier commits. If a credential is exposed,
revoke or rotate it at its provider and update its consumers. History cleanup
does not replace provider-side revocation.
