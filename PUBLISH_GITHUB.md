# Publishing RodriguesProject on GitHub

## Recommended repository settings

- Repository name: `RodriguesProject`
- Visibility: **Public**
- Initialize with README: **No** when uploading this prepared package (the repository already contains a README)
- Add `.gitignore`: **No** (already included)
- License: **No additional license selection** (MIT is already included)

## Option A — Git command line

From the root of this folder:

```bash
git init
git branch -M main
git add .
git commit -m "feat: add judicial QA engineering portfolio"
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/RodriguesProject.git
git push -u origin main
```

Replace `YOUR_GITHUB_USERNAME` with your actual GitHub username.

## Option B — GitHub web interface

1. Create a new public repository named `RodriguesProject`.
2. Do not initialize it with another README, `.gitignore` or license.
3. Upload the contents of this folder to the repository root.
4. Commit the files to the `main` branch.
5. Confirm that `README.md`, `tests/` and `.github/workflows/qa.yml` are visible at the repository root.
6. Open **Actions** and confirm that the QA workflow runs successfully.

## Recommended repository description

`QA Engineering portfolio: test planning, functional/integration/E2E/regression testing, API testing, security testing, Pytest automation and GitHub Actions using a fictional judicial information system.`

## Suggested topics

`qa`, `software-testing`, `quality-assurance`, `python`, `pytest`, `fastapi`, `api-testing`, `test-automation`, `regression-testing`, `security-testing`, `github-actions`, `judicial-tech`

## Recruiter-facing profile

After publishing, pin `RodriguesProject` to your GitHub profile. GitHub allows up to six repositories/gists to be pinned on a profile.

## Important

Keep the portfolio disclaimer intact. Never present this fictional project as professional work for UNDP, CNJ, a court, a government agency or another real institution.
