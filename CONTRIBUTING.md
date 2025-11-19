# Contributing to RoamEN

Thank you for your interest in contributing to RoamEN! This project aims to provide reliable emergency communication for healthcare and emergency response scenarios.

## How to Contribute

### Reporting Bugs

If you find a bug:

1. **Check existing issues** first to avoid duplicates
2. **Create a new issue** with:
   - Clear title
   - Detailed description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment (OS, Python version, hardware)
   - Relevant logs or screenshots

### Suggesting Features

For new features:

1. **Check existing issues** and discussions
2. **Open a discussion** first if it's a major change
3. **Create an issue** with:
   - Use case description
   - Proposed solution
   - Alternatives considered
   - Impact on existing functionality

### Contributing Code

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes**
4. **Test thoroughly**:
   ```bash
   cd firmware/node
   python3 test_roamen.py
   ```
5. **Commit with clear messages**:
   ```bash
   git commit -m "Add feature: description"
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

## Development Setup

See [Development Setup Guide](docs/guides/DEVELOPMENT_SETUP.md) for detailed instructions.

Quick setup:
```bash
git clone https://github.com/mb43/roamen.git
cd roamen
pip3 install -r firmware/node/requirements.txt
cd firmware/node
python3 test_roamen.py
```

## Code Style

### Python

- **PEP 8** style guide
- **Type hints** for function signatures
- **Docstrings** for public functions (Google style)
- **Line length**: 100 characters max
- **Imports**: Organize alphabetically, grouped by stdlib/third-party/local

Example:
```python
def create_packet(source_id: int, dest_id: int, message: str) -> RoamENPacket:
    """Create a text message packet.

    Args:
        source_id: Source node ID (1-65534)
        dest_id: Destination node ID (1-65534 or 0xFFFF for broadcast)
        message: Message text (max 256 bytes UTF-8)

    Returns:
        RoamENPacket ready for transmission

    Raises:
        ValueError: If source_id or dest_id is invalid
    """
    payload = message.encode('utf-8')[:256]
    return RoamENPacket(
        packet_type=PacketType.TEXT_MESSAGE,
        source_id=source_id,
        dest_id=dest_id,
        priority=Priority.NORMAL,
        payload=payload
    )
```

### Documentation

- **Markdown** for all documentation
- **Clear headings** and structure
- **Code examples** where relevant
- **Links** to related docs

## Testing

### Unit Tests

All new code should include tests:

```python
def test_new_feature():
    """Test description"""
    # Arrange
    input_data = ...

    # Act
    result = function_to_test(input_data)

    # Assert
    assert result == expected_value
    assert isinstance(result, ExpectedType)

    print("  ✅ Test description passed")
```

Run tests:
```bash
cd firmware/node
python3 test_roamen.py
```

All tests must pass before merging.

### Integration Tests

For features involving multiple components:

```python
def test_integration():
    """Test multiple components together"""
    # Create components
    sender = Node(id=1)
    receiver = Node(id=2)

    # Test interaction
    packet = sender.create_message("Test")
    data = sender.transmit(packet)
    received = receiver.receive(data)

    # Verify
    assert received.payload == packet.payload
```

### Hardware Tests

If adding hardware-specific code:

- Document required hardware
- Provide simulation/mock for testing without hardware
- Test on actual hardware before submitting PR

## Commit Messages

Follow conventional commits:

- `feat: Add voice transmission support`
- `fix: Correct CRC calculation for large packets`
- `docs: Update protocol specification`
- `test: Add tests for alert packets`
- `refactor: Simplify packet encoding`
- `chore: Update dependencies`

Keep first line under 72 characters.

## Pull Request Process

1. **Update documentation** if behavior changes
2. **Add tests** for new features
3. **Update CHANGELOG.md** (if exists)
4. **Ensure all tests pass**
5. **Request review** from maintainers
6. **Address review comments**
7. **Squash commits** if requested
8. **Wait for approval** before merging

### PR Template

When creating a PR, include:

```markdown
## Description
Brief description of changes

## Motivation
Why is this change needed?

## Changes
- List of specific changes
- Modified files
- New functionality

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed
- [ ] Tested on hardware (if applicable)

## Documentation
- [ ] Code comments added
- [ ] Docstrings updated
- [ ] README updated (if needed)
- [ ] Technical docs updated (if needed)

## Breaking Changes
List any breaking changes and migration path

## Related Issues
Fixes #123, relates to #456
```

## Areas Needing Contribution

### High Priority

- **FreeDV Integration**: Implement voice codec integration
- **Radio Interface**: Complete SDR abstraction layer
- **Mesh Routing**: Implement basic routing algorithm
- **Web UI**: Create user interface for node management

### Medium Priority

- **Encryption**: AES-256 implementation
- **Key Management**: Secure key distribution
- **Network Diagnostics**: Tools for debugging
- **Mobile App**: iOS/Android client

### Low Priority

- **Additional Codecs**: Alternative voice codecs
- **File Transfer**: Reliable file transmission
- **GPS Integration**: Location tracking
- **Advanced Routing**: Optimized mesh algorithms

## Code Review Guidelines

### For Contributors

- **Be responsive** to feedback
- **Explain your approach** in comments
- **Update based on feedback**
- **Be patient** - reviews take time

### For Reviewers

- **Be constructive** and respectful
- **Explain why** changes are needed
- **Suggest alternatives** where appropriate
- **Approve quickly** if code is good

## Documentation Contributions

Documentation is as important as code!

**Areas needing help**:
- User guides
- API documentation
- Tutorial videos
- Deployment guides
- Troubleshooting guides

**Style guide**:
- Clear, concise language
- Step-by-step instructions
- Screenshots where helpful
- Examples for all features

## Community Guidelines

### Code of Conduct

- **Be respectful** to all contributors
- **Be inclusive** of different backgrounds
- **Be collaborative** and helpful
- **Be patient** with newcomers
- **No harassment** of any kind

### Communication

- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: General questions, ideas
- **Pull Requests**: Code contributions
- (Future: Discord/Slack for real-time chat)

### Getting Help

If you need help:

1. Check existing documentation
2. Search issues and discussions
3. Ask in GitHub Discussions
4. Tag relevant maintainers

## Release Process

(For maintainers)

1. **Update version** in relevant files
2. **Update CHANGELOG.md**
3. **Run full test suite**
4. **Create release tag**: `git tag -a v1.0.0 -m "Release v1.0.0"`
5. **Push tag**: `git push origin v1.0.0`
6. **Create GitHub release** with notes
7. **Announce** in discussions

## Legal

By contributing, you agree that your contributions will be licensed under GPL-3.0.

### Contributor License Agreement

You certify that:

1. The contribution is your original work
2. You have the right to submit the contribution
3. You agree to the GPL-3.0 license
4. You understand this is a public project

## Recognition

Contributors will be:

- Listed in CONTRIBUTORS.md (if exists)
- Mentioned in release notes
- Credited in any publications about the project

Significant contributors may be invited to become maintainers.

## Questions?

If you have questions about contributing:

- Open a discussion on GitHub
- Review existing issues and PRs
- Check the documentation

Thank you for making RoamEN better! 🚀

---

**Last Updated**: 2025-11-19
**Version**: 1.0
