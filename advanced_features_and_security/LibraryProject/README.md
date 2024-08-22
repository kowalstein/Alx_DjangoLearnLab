# Django Permissions and Groups Setup

## Custom Permissions

The `Article` model includes the following custom permissions:
- `can_view`: Allows viewing articles.
- `can_create`: Allows creating new articles.
- `can_edit`: Allows editing existing articles.
- `can_delete`: Allows deleting articles.

## Groups and Permissions

### Groups Created:
- **Editors**: Assigned `can_edit` and `can_create` permissions.
- **Viewers**: Assigned `can_view` permission.
- **Admins**: Assigned all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).

## Usage in Views

- Use `@permission_required('bookshelf.can_view', raise_exception=True)` to restrict access to views based on permissions.

## Testing

- Test users should be created and assigned to appropriate groups.
- Ensure that users can only access views and perform actions based on their permissions.
