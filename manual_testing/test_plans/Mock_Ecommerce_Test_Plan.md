# Test Plan: E-Commerce Web Application (Mock)

## 1. Introduction
This document outlines the testing strategy, scope, and resources required for testing the core functionality of the Mock E-Commerce Web Application. The goal is to ensure a seamless shopping experience for end users.

## 2. Scope
### In-Scope
- User Authentication (Login, Registration, Password Reset)
- Product Search & Filtering
- Shopping Cart functionality
- Checkout Process (Guest and Registered User)
- Payment Gateway Integration (Stripe Mock)

### Out-of-Scope
- Backend inventory management system (Admin panel)
- Load & Performance testing (covered in a separate phase)

## 3. Test Strategy
We will employ a combination of **Manual Exploratory Testing** and **Automated Regression Testing**.
- **UI/Functional:** Manual tests executed across Chrome, Firefox, and Safari.
- **API Testing:** Automated Pytest scripts validating JSON responses and status codes.
- **Defect Tracking:** Jira (mocked). Bug reports will include severity, priority, and Steps to Reproduce (STR).

## 4. Test Environment
- **OS:** Windows 11, macOS Ventura, iOS 16, Android 13
- **Browsers:** Chrome (v114+), Safari (v16.5+), Firefox (v113+)
- **Staging URL:** `https://staging.mock-ecommerce.com`

## 5. Deliverables
1. Comprehensive Test Cases Matrix
2. API Automation Test Suite (Pytest)
3. Defect Reports
4. Final Test Execution Summary Report

---
*Prepared by: QA Engineer / SDET*
