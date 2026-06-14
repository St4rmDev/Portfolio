# Bug Report: BUG-001

**Title:** Critical crash during Guest Checkout when applying expired promo code.
**Project:** Mock E-Commerce Web Application
**Environment:** Staging (`https://staging.mock-ecommerce.com`)
**Browser/OS:** Google Chrome v114 / macOS Ventura
**Severity:** 🔴 Critical
**Priority:** 🔴 High

## Description
When an unauthenticated user (guest) attempts to apply an expired promotional code at the final checkout step, the application throws a 500 Internal Server Error instead of displaying a graceful validation message. This completely blocks the user from completing their purchase.

## Steps to Reproduce (STR)
1. Navigate to `https://staging.mock-ecommerce.com`.
2. Add any item (e.g., "Wireless Headphones") to the shopping cart.
3. Proceed to Checkout and select "Continue as Guest".
4. Fill out the shipping and billing forms with valid mock data.
5. In the "Order Summary" section, enter the expired promo code: `SUMMER25`.
6. Click the "Apply" button.

## Expected Result
An inline validation error message should appear in red text stating: "This promo code has expired or is invalid." The checkout process should remain active.

## Actual Result
The page crashes, displaying a standard white-screen `500 Internal Server Error`. The browser console shows an unhandled exception: `TypeError: Cannot read properties of null (reading 'discount_value')`.

## Attachments
- `checkout_crash_screenshot.png` (Mock)
- `browser_console.log` (Mock)

## Triage Notes
This appears to be a backend API issue where the validation controller fails to handle a null return from the database query for expired codes.
