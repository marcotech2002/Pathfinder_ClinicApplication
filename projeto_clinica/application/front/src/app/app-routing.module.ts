import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: "", redirectTo: "authentication", pathMatch: 'full' },
  { path: "authentication", loadChildren: () => import("../app/authentication/authentication.module").then(m => m.AuthenticationModule) },
  { path: "main", loadChildren: () => import("../app/main/main.module").then(m => m.MainModule) }
  //{ path: '**', component: PageNotFoundComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
