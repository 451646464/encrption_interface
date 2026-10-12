# Encryption Interface

<p align="center">
  <strong>A Python desktop application for learning and experimenting with encryption and decryption</strong>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white">
  <img alt="GUI" src="https://img.shields.io/badge/GUI-Tkinter-2C7A7B">
  <img alt="Cryptography" src="https://img.shields.io/badge/Topic-Cryptography-6C3483">
  <img alt="Platform" src="https://img.shields.io/badge/Platform-Desktop-lightgrey">
</p>

## Overview

**Encryption Interface** is a Python desktop GUI project that brings several text-encryption, decryption, and file-encryption demonstrations together in one interface. Built with Tkinter, it lets users select an available algorithm, enter text, and run supported operations through a graphical application.

The repository includes classical ciphers for educational use, hashing functionality, and file-encryption operations using the `cryptography` package. It is designed as a hands-on cryptography learning project—not as a replacement for a reviewed, production-grade encryption product.

## Features

### Text operations

The interface includes implementations or options for algorithms such as:

- **Caesar Cipher** — a basic substitution cipher.
- **Reverse Cipher** — reverses text as a simple demonstration.
- **Autokey** — a classical polyalphabetic cipher.
- **Vigenère Cipher** — a classical cipher using a repeating or derived key.
- **One-Time Pad** — a classical technique whose security depends on strict key-generation and key-use requirements.
- **Hashing** — generates a hash digest where supported.
- **Custom and transfer-related options** — additional methods implemented in the application.

The exact behavior and supported inputs depend on the implementation in `main.py`.

### File operations

The application also provides file-encryption actions for supported file types, including images, PDF documents, audio, and video. The repository describes these operations as using Fernet symmetric encryption through the Python `cryptography` library.

Encrypted output should be treated as sensitive data. Keep a secure backup of the original file and any key required for decryption.

### Graphical interface

- Desktop interface built with Python Tkinter.
- Algorithm selection through the GUI.
- Text input and output for supported operations.
- Buttons and dialogs for user-driven processing and file selection.

## Technology Stack

- **Python** — application logic.
- **Tkinter** — desktop graphical interface.
- **cryptography** — cryptographic primitives and Fernet-based file encryption.
- **hashlib** — hash functions available in Python's standard library.

## Repository Structure

```text
encrption_interface/
├── main.py       # GUI and encryption/decryption implementation
└── README.md     # Project documentation
```

This reflects the main files currently shown in the repository. The structure may change as the project develops.

## Getting Started

### Prerequisites

- Python 3 installed.
- `pip`, Python's package installer.
- The `cryptography` package for features that depend on it.
- Tkinter available in your Python installation. It is commonly included with Python on Windows; some Linux distributions package it separately.

### 1. Clone the repository

```bash
git clone https://github.com/451646464/encrption_interface.git
cd encrption_interface
```

### 2. Install the dependency

```bash
python -m pip install cryptography
```

If the project later includes a `requirements.txt`, install dependencies from that file instead:

```bash
python -m pip install -r requirements.txt
```

### 3. Run the application

```bash
python main.py
```

On systems where Python 3 is invoked as `python3`, use:

```bash
python3 main.py
```

## How to Use

1. Start the application.
2. Choose an available algorithm or operation from the interface.
3. Enter the text and any key or parameters required by that operation.
4. Select the relevant encrypt, decrypt, or process action.
5. For supported file operations, choose the input file when prompted and keep track of the encrypted output and decryption key.
6. Verify results with test data before using the tool on important files.

The controls and supported formats are defined by the current `main.py` implementation.

## Cryptography and Security Notes

This project combines educational classical ciphers with file-encryption functionality. These are not equivalent security mechanisms.

- **Caesar, Reverse, Autokey, and Vigenère ciphers are not suitable for protecting sensitive information.** They are useful for learning concepts, not for modern security.
- **A hash is not encryption.** Hashing is generally one-way and does not provide a way to recover the original text.
- **Fernet requires correct key handling.** If the key is lost, encrypted data may be unrecoverable. If an attacker obtains the key, they may be able to decrypt the data.
- Keep keys separate from encrypted files and never publish keys, passwords, or confidential input in the repository.
- Test with copies of files. Do not rely on an experimental tool as the only protection for important data.
- For real-world applications, use well-reviewed modern cryptographic libraries and established protocols rather than designing custom cryptographic algorithms.

## Limitations

- The project is primarily an educational desktop application.
- Classical cipher implementations are not secure against modern cryptanalysis.
- Supported file types, key handling, error handling, and output naming depend on the current code.
- No claim of independent security audit or production readiness is made.

## Contributing

Suggestions, bug reports, and improvements are welcome.

1. Fork the repository.
2. Create a branch for your change.
3. Test the change with non-sensitive sample data.
4. Submit a pull request describing the change and any security implications.

## License

No license terms are documented in this README. Check the repository for a `LICENSE` file or add a suitable license before redistributing or reusing the project.

## Developer

**Rakan Almoliki (راكان المليكي)**

- **Email:** [rakanalmoliki33@gmail.com](mailto:rakanalmoliki33@gmail.com)
- **GitHub:** [451646464](https://github.com/451646464)

---

If you find this project useful, consider giving the repository a star.
