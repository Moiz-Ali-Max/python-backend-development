# Workflow State Manager (OOP-heavy)

### Purpose

- OOP
- Role-based access
- Exception handling
- Decorators

### What you have to build?
#### 1. Core Entities (Classes)
##### User
- id
- name
- role (admin / manager / user)
##### Request
- request_id
- title
- current_status
- (created → approved → rejected)

#### 2. Decorator (Mandatory)
Create
```
@require_role("admin")
```
Used on:
- approve_request()
- reject_request()

If role mismatch:
```
Access denied
```

#### 3. Business Rules

- User can create request
- Only admin can approve/reject
- Approved request cannot be changed
- Invalid transitions raise exceptions

#### 4. Output

Print:
- request history
- final state
- meaningful errors

#### Example Workflow:
Step 1: User create the request
```
Ali created request: Laptop Purchase
Status: CREATED
```

Step 2: User try to approve 
```
Ali tries to approve request
Access denied: requires admin
```

Step 3: Admin approves
```
Sara approved request
Status changed to APPROVED
```

Step 4: Again try to approve/reject
```
Error: Approved request cannot be modified
```
