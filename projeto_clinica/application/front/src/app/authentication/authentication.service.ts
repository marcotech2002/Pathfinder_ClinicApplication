import { Injectable } from '@angular/core';
import { User } from '../models/user';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  private userAuthenticated: boolean = false;

  constructor(private router: Router) { }

  Login(user: User){
    if(user.email == "marco@gmail.com" && user.password == "123456"){
      this.userAuthenticated = true;
      this.router.navigate(["/main"]);
    }
    else{
      this.userAuthenticated = false;
    }
  }
}
