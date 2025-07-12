# ReWear-Community-Clothing-Exchange
ReWear Login Page
Overview
This project contains a simple login page for the ReWear application, a platform focused on sustainable fashion. The page is built using pure HTML and CSS, with minimal JavaScript for form handling and password visibility toggling. It replicates the design and functionality of a React/TSX-based login component, styled with Tailwind CSS-inspired aesthetics.
Features

Responsive Design: Adapts to various screen sizes with a centered layout.
Gradient Styling: Uses gradients for the background, logo, and button to match the ReWear brand.
Password Toggle: Allows users to show/hide the password field with an eye icon.
Form Validation: Basic client-side validation ensures email and password fields are filled before submission.
Navigation: Includes links to home, registration, and forgot password pages (placeholders).
Alert Feedback: Displays success or error messages using alerts (replacing toast notifications).

File Structure


├── index.html # Login page
├── signup.html # User registration page
├── landingpage.html # Main landing/home page
├── listitem.html # Page for users to list their clothing items
├── assets/ # External JS, CSS files linked via Lovable or Vite
├── styles/ # (Optional) Custom styles folder
├── images/ # Hosted or CDN image assets
└── README.md # Project documentation (this file)

Setup Instructions

Clone or Download: Obtain the index.html file.
Open in Browser: Open index.html directly in a web browser (no server required, as it uses a CDN for icons).
Ensure Internet Access: The Lucide Icons CDN requires an internet connection to load icons.

Usage

Form Submission: Enter an email and password, then click "Sign In". If both fields are filled, an alert welcomes the user and redirects to a placeholder /dashboard page. If fields are empty, an error alert is shown.
Password Toggle: Click the eye icon next to the password field to toggle between showing and hiding the password.
Navigation Links:
"Back to Home" links to /.
"Sign up here" links to /register.
"Forgot Password?" is a placeholder link (#).


Styling: The page uses a gradient background, a glass-effect card, and hover animations for a modern look.

Customization

Styling: Modify the <style> section in index.html to adjust colors, fonts, or layout.
Icons: Replace Lucide icons by updating the CDN or using a different icon library.
Form Handling: Update the JavaScript in the <script> section to integrate with a backend API for actual authentication.
Links: Update placeholder URLs (/dashboard, /register, #) to point to actual routes.


 Key Features

- 🌱 **Eco-Friendly Swaps** – Exchange pre-loved clothes easily
- 🎯 **Point-Based System** – Earn points for items and redeem fashion pieces
- 👥 **Community Powered** – Built for fashion-conscious users
- 📱 **Responsive UI** – Smooth layout across all devices
- 🔐 **Login & Register** – Secure user management
- 📦 **Featured Items** – Curated collection from the community
  
 Technology Stack 
 
| **Category**      | **Technology**                         | **Purpose**                                                              |
| ----------------- | -------------------------------------- | ------------------------------------------------------------------------ |
| 🌐 Front-End      | HTML5, CSS3                            | Core structure and styling of the application                            |
| 🎨 UI Styling     | Custom CSS (Tailwind-inspired)         | Responsive layouts, gradients, and glassmorphism design                  |
| ⚙️ Interactivity  | JavaScript (Vanilla)                   | Handles form validation, password toggle, and alert messages             |
| 🧩 Icons          | Lucide Icons (via CDN)                 | Modern, lightweight icon set for UI clarity                              |                         | 📦 File Hosting   | GitHub Pages / Local browser           | Project runs directly in a browser with no backend needed                |
| 🚀 Present Scope  | Backend API (Firebase, etc.)          | For authentication, data storage, and swap transactions *(future-ready)* |
|    Backend        | flask , python ( libraies)             |To build RESTful APIs for login, registration, item listing, swap handling |

Notes

This is a front-end-only implementation. For production, integrate with a backend for secure authentication.
The alert-based feedback mimics the original toast notifications but can be enhanced with a proper toast library.
The design is optimized for modern browsers (Chrome, Firefox, Safari, Edge).
image:-
![WhatsApp Image 2025-07-12 at 14 16 04_7e807b09](https://github.com/user-attachments/assets/a62270aa-1323-4d89-8a7b-81d0082dc508)
<img width="995" height="934" alt="image" src="https://github.com/user-attachments/assets/b45dd1ff-d91a-4a3a-aab2-542c4fafe769" />
![WhatsApp Image 2025-07-12 at 15 40 47_ad72dd39](https://github.com/user-attachments/assets/e6e16f90-044e-444c-aaa6-47e9044f9d30)
![WhatsApp Image 2025-07-12 at 15 42 17_f9cf8bc7](https://github.com/user-attachments/assets/34460919-5eea-40fa-8428-4ae214fbb378)
![WhatsApp Image 2025-07-12 at 15 43 08_0be464bc](https://github.com/user-attachments/assets/de8b087b-e710-4356-b9ad-705483ad854a)
![WhatsApp Image 2025-07-12 at 15 46 27_05bf5662](https://github.com/user-attachments/assets/f31dc86f-70a5-43e7-bd87-7d7dbbc64dd5)
<img width="1280" height="653" alt="image" src="https://github.com/user-attachments/assets/02553c81-eda5-4e87-a137-d5da2a70bd25" />
<img width="1280" height="628" alt="image" src="https://github.com/user-attachments/assets/23af8a31-11c4-4b06-92f3-521b2057cd52" />
<img width="1280" height="665" alt="image" src="https://github.com/user-attachments/assets/aec98ab7-6687-4f2d-93a4-e8bc7637c2d0" />
<img width="1280" height="658" alt="image" src="https://github.com/user-attachments/assets/95e0ef39-5f72-461c-9764-c3fad010eeb9" />
<img width="1280" height="608" alt="image" src="https://github.com/user-attachments/assets/13344a31-9ac1-48a5-b162-fcfa8634a2f8" />


 Clean and Eco-Friendly Design:
Minimalist layout with green tones that align with the sustainable fashion theme, making the interface visually appealing and purposeful.

User-Friendly Form Fields:
Clearly labeled inputs for full name, email, password, and password confirmation with helpful placeholders and a password visibility toggle.

Terms & Privacy Compliance:
Includes a mandatory checkbox for agreeing to the Terms of Service and Privacy Policy, ensuring user consent before account creation.

Call-to-Action with Visual Emphasis:
A prominent "Create Account" button with a soft green gradient encourages user interaction and aligns with the app’s eco-conscious branding.









Tanushka Tomar-tanushkat2005@gmail.com
Mahek Gupta-eshueshu22gupta@gmail.com
Satya Mishra-satyamishra0611@gmail.com
Dharmesh Krish Mitaulia-gamep8549@gmail.com
