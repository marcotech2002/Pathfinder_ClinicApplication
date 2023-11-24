import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { LoginComponent } from './login/login.component';
import { ResetPasswordComponent } from './reset-password/reset-password.component';
import { LoginRegistrationComponent } from './login-registration/login-registration.component';


const authenticationRoutes: Routes = [
  { path: "", component: LoginComponent },
  { path: "reset-password", component: ResetPasswordComponent},
  { path: "login-registration", component: LoginRegistrationComponent }
];

@NgModule({
  imports: [RouterModule.forChild(authenticationRoutes)],
  exports: [RouterModule]
})
export class AuthenticationRoutingModule { }
