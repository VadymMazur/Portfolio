This repository contains examples and explanations related to requirements analysis. It aims to illustrate best practices and common pitfalls in defining clear, testable, and unambiguous requirements.  The project includes sample requirements for a monitor and smartphone, along with a set of functional and non-functional requirements for a hypothetical pet photo sharing application.

## Examples of Requirements

### Monitor:

*   **Refresh Rate:** The screen refresh rate must be 144 Hz (a testability).
*   **Resolution:** The monitor resolution is 3840x2160 pixels (n/non-contradiction).
*   **Brightness:** The screen brightness must be at least 350 cd/m² (testability).
*   **Diagonal Size:** The display must have a diagonal size of 27 inches (verifiability).

### Smartphone:

*   **Battery Capacity:** The battery capacity is 5000 mAh.
*   **Operating System:** The smartphone runs on Android 16 (consistency/non-contradiction).
*   **Charging Time:**  The time to fully charge the battery is 77 minutes (testability).
*   **Screen Refresh Rate:** The screen refresh rate is 120 Hz (verifiability).

## Requirements Analysis Technique

In my opinion, **formal inspection combined with graphical visualization and prototyping** provides the highest quality results.  Engaging a broad range of stakeholders (QA engineers, developers, business analysts, UX designers) allows for identifying inconsistencies from various perspectives and avoiding blind spots. Visualizing requirements through diagrams, mockups, and interactive prototypes helps all participants achieve a shared understanding of the system and proactively identify potential issues before development begins – significantly reducing risks and costs.

## Functional Requirements for the Application (Pet Photo Sharing App Example)

*   Login via social media accounts (Google, Facebook).
*   Create and edit user profiles (avatar, name, bio).
*   Upload photos of pets with descriptions.
*   Publish photos to a news feed.
*   Search for photos and posts by hashtag.
*   Like photos.
*   Receive push notifications for new likes or comments.

## Non-Functional Requirements for the Application

*   The application must run on iOS and Android platforms.
*   Main screen loading time should be less than 2 seconds.
*   Maximum photo upload size: 1080x1920 pixels.
*   User interface must be user-friendly, intuitive, and adaptive to various screen sizes.
*   All user data must be transmitted over an encrypted HTTPS connection.
*   The application should support offline viewing of previously downloaded photos.
*   The user interface must be localized into English and Ukrainian languages.

