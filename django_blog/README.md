## Blog Post Management

This Django application supports full CRUD operations for blog posts.

### Features
- **List Posts:** Display all blog posts.
- **View Post:** Detailed view of a single post.
- **Create Post:** Form for authenticated users to create a new post.
- **Edit Post:** Form for post authors to edit their posts.
- **Delete Post:** Option for post authors to delete their posts.

### Permissions
- **Authenticated Users:** Can create posts.
- **Post Authors:** Can edit and delete their posts.
- **Public:** Can view the list and details of all posts.

### Testing
1. **Create Post:** Test creating a new post.
2. **Edit Post:** Verify only the author can edit.
3. **Delete Post:** Ensure only the author can delete.
4. **List and Detail Views:** Confirm accessibility for all users.
