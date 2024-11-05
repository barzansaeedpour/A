

## session 1:

- creating the project and apps
- creating urls
- creating templates
- creating views

## session 2:

- Custom User

    - https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#substituting-a-custom-user-model
    - https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#a-full-example

- User Manager

    - https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model

- User Creation & Changing Forms
    - https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#a-full-example


- User Register
    - UserRegistrationForm
    - UserRegisterView
    - urlpatterns
    - accounts/templates/register.html

## session 3:

    - Generate and send random code to user for registration
      - Otp Model
      - OtpCodeAdmin
    
    - Register & Sessions
      - https://docs.djangoproject.com/en/5.1/topics/http/sessions/
      - When the sessions are saved?
      - utils (send otp code by sms)
      - accounts.views (UserRegisterView.post)
      - accounts.forms (VerifyCodeForm)
      - accounts.views (UserRegisterVerifyCodeView)
      - accounts.templates (verify.html)
      - utils (kavenegar)
    
    - Static & Media files
      - What is the difference?
      - home/static/home/css -> base.html, home.html
      - Static files directory -> for all of the apps -> base.html

## Session 4:
    - Models (home/models)
        - Category
            - verbose_name, verbose_name_plural
        - Product (Image Field, Pillow) -> Python data time field
    
    - Register Models in admin

    - Media Files (https://docs.djangoproject.com/en/5.1/ref/settings/#std-setting-MEDIA_ROOT)
        - MEDIA_ROOT -> Absolute filesystem path to the directory that will hold user-uploaded fiels
        - MEDIA_URL -> Url that handles the media served from MEDIA_ROOT

