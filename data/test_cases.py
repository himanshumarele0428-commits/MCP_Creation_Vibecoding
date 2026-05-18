"""
Data File 1: Test Cases Repository
TheTestingAcademy | Dummy Playwright Test Case Data
"""

TEST_CASES_DATA = {
    "metadata": {
        "source": "TheTestingAcademy QA Repository",
        "version": "3.1.0",
        "last_updated": "2026-05-19",
        "total_cases": 24
    },
    "test_cases": [
        {
            "id": "TC-001",
            "title": "Verify successful login with valid credentials",
            "module": "Login & Authentication",
            "priority": "Critical",
            "type": "Smoke",
            "status": "Pass",
            "automation": True,
            "steps": [
                "Navigate to https://thetestingacademy.com/login",
                "Enter valid username in #email field",
                "Enter valid password in #password field",
                "Click 'Login' button",
                "Assert redirect to /dashboard"
            ],
            "expected": "User is redirected to the dashboard with a welcome message."
        },
        {
            "id": "TC-002",
            "title": "Verify login fails with invalid credentials",
            "module": "Login & Authentication",
            "priority": "Critical",
            "type": "Regression",
            "status": "Pass",
            "automation": True,
            "steps": [
                "Navigate to /login",
                "Enter invalid username",
                "Enter invalid password",
                "Click 'Login' button",
                "Assert error message is visible"
            ],
            "expected": "Error message 'Invalid credentials' is displayed."
        },
        {
            "id": "TC-003",
            "title": "Verify password field masks input",
            "module": "Login & Authentication",
            "priority": "High",
            "type": "Functional",
            "status": "Pass",
            "automation": True,
            "steps": [
                "Navigate to /login",
                "Click on password field",
                "Type any password",
                "Assert input type is 'password'"
            ],
            "expected": "Password characters are masked."
        },
        {
            "id": "TC-004",
            "title": "Verify course list loads on dashboard",
            "module": "Dashboard",
            "priority": "High",
            "type": "Smoke",
            "status": "Pass",
            "automation": True,
            "steps": [
                "Login with valid credentials",
                "Wait for dashboard to load",
                "Assert '.course-card' elements are visible",
                "Assert count >= 3"
            ],
            "expected": "At least 3 course cards are rendered on the dashboard."
        },
        {
            "id": "TC-005",
            "title": "Verify user can enroll in a course",
            "module": "Course Management",
            "priority": "Critical",
            "type": "E2E",
            "status": "Fail",
            "automation": True,
            "steps": [
                "Login with valid credentials",
                "Navigate to a course page",
                "Click 'Enroll Now' button",
                "Confirm payment modal appears",
                "Assert enrollment success message"
            ],
            "expected": "User is enrolled and sees confirmation banner.",
            "failure_reason": "Payment modal does not appear on staging env."
        },
        {
            "id": "TC-006",
            "title": "Verify search returns relevant courses",
            "module": "Search & Filters",
            "priority": "Medium",
            "type": "Functional",
            "status": "Pass",
            "automation": True,
            "steps": [
                "Navigate to /courses",
                "Type 'Playwright' in search bar",
                "Press Enter",
                "Assert results contain 'Playwright' in titles"
            ],
            "expected": "Search results display Playwright-related courses."
        },
        {
            "id": "TC-007",
            "title": "Verify user profile page displays correct info",
            "module": "User Profile",
            "priority": "Medium",
            "type": "Regression",
            "status": "Pass",
            "automation": False,
            "steps": [
                "Login with valid credentials",
                "Click on user avatar",
                "Select 'My Profile'",
                "Assert name, email, and avatar are visible"
            ],
            "expected": "Profile page shows accurate user information."
        },
        {
            "id": "TC-008",
            "title": "Verify logout clears session",
            "module": "Login & Authentication",
            "priority": "High",
            "type": "Security",
            "status": "Pass",
            "automation": True,
            "steps": [
                "Login with valid credentials",
                "Click logout button",
                "Navigate to /dashboard directly",
                "Assert redirect to /login"
            ],
            "expected": "Session is cleared and user is redirected to login."
        },
        {
            "id": "TC-009",
            "title": "Verify admin can deactivate a user account",
            "module": "Admin Panel",
            "priority": "High",
            "type": "Functional",
            "status": "Pending",
            "automation": False,
            "steps": [
                "Login as admin",
                "Navigate to /admin/users",
                "Find user and click 'Deactivate'",
                "Confirm action in modal",
                "Assert user status shows 'Inactive'"
            ],
            "expected": "User account is marked as inactive in the admin panel."
        },
        {
            "id": "TC-010",
            "title": "Verify payment gateway processes mock payment",
            "module": "Payment Gateway",
            "priority": "Critical",
            "type": "E2E",
            "status": "Flaky",
            "automation": True,
            "steps": [
                "Navigate to checkout",
                "Enter test card details",
                "Click 'Pay Now'",
                "Assert success page with order ID"
            ],
            "expected": "Payment confirmation page shown with order ID.",
            "failure_reason": "Intermittent 502 from payment provider sandbox."
        },
        {
            "id": "TC-011",
            "title": "Verify email notification is sent after enrollment",
            "module": "Notifications",
            "priority": "Medium",
            "type": "Integration",
            "status": "Pass",
            "automation": False,
            "steps": [
                "Enroll in a course",
                "Check registered email inbox",
                "Assert email subject contains 'Enrollment Confirmed'"
            ],
            "expected": "Confirmation email received within 2 minutes."
        },
        {
            "id": "TC-012",
            "title": "Verify course filter by category works correctly",
            "module": "Search & Filters",
            "priority": "Low",
            "type": "Functional",
            "status": "Pass",
            "automation": True,
            "steps": [
                "Navigate to /courses",
                "Select 'Automation' from category dropdown",
                "Assert all displayed courses belong to 'Automation'"
            ],
            "expected": "Only automation courses are displayed after filtering."
        }
    ]
}
