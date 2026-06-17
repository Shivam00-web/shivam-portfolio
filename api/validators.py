from django.core.validators import FileExtensionValidator

ALLOWED_LOGO_EXTENSIONS = ['svg', 'png', 'jpg', 'jpeg', 'webp']

logo_file_validator = FileExtensionValidator(
    allowed_extensions=ALLOWED_LOGO_EXTENSIONS,
    message='Upload a valid logo file (SVG, PNG, JPG, JPEG, or WebP).',
)

cv_file_validator = FileExtensionValidator(
    allowed_extensions=['pdf'],
    message='Upload a valid PDF file.',
)
