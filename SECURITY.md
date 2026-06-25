# Security Policy

## Supported Versions

This project is an educational simulator. Security reports are accepted for the current `main` branch.

## Reporting a Vulnerability

Please do not disclose suspected vulnerabilities publicly before maintainers have reviewed them.

Report security issues by opening a private security advisory on GitHub, or by contacting the maintainers through the repository owner profile if private advisories are unavailable.

Include:

- affected module or algorithm wrapper
- Python and dependency versions
- steps to reproduce
- impact assessment
- suggested fix, if known

## Scope

In scope:

- unsafe dependency usage
- incorrect verification or validation behavior
- accidental secret exposure in logs or generated files
- reproducible denial-of-service behavior caused by project code

Out of scope:

- theoretical breaks in upstream cryptographic algorithms
- vulnerabilities in dependencies that should be reported upstream
- requests to use this simulator as a production cryptographic system

## Cryptography Notice

This project is for education and benchmarking. It is not audited and must not be used to protect production data.
