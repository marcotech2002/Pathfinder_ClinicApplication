import { Component, OnInit } from '@angular/core';
import { AuthenticationService } from '../authentication.service';
import { User } from 'src/app/models/user';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { ModalComponent } from 'src/app/extra/modal/modal.component';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  private user: User = new User();
  form: any;

  constructor(
    private authenticationService: AuthenticationService,
    private dialog: MatDialog
  ) { }

  ngOnInit(): void {
    this.form = new FormGroup({
      email: new FormControl("", [Validators.email, Validators.required]),
      password: new FormControl("", [Validators.required])
    });
  }

  openDialog(title: string, content: string): void {
    const dialogRef = this.dialog.open(ModalComponent, {
      data: {title: title, content: content},
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
    });
  }

  Login(){ 
    this.user.email = this.form.controls["email"].value;
    this.user.password = this.form.controls["password"].value;

    if(this.user.email && this.user.password){
      this.authenticationService.Login(this.user);
    }
    else{
      this.openDialog("Aviso", "Formulário incompleto!");
    }
  }

}
