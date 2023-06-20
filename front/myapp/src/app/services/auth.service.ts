import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
// import { Http, Headers, Response } from '@angular/http';
@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(private http: HttpClient) {}
  SERVER_URL = 'http://127.0.0.1:8000/';
  

  checkOut(cart: any[]): Observable<any> {
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${localStorage.getItem('token')}`
    });
  
    return this.http.post<any>(this.SERVER_URL + 'checkout', cart, { headers: headers });
  }


  // checkOut(cart:any[]): Observable<any> {
  //   const headers = new HttpHeaders({
  //     'Content-Type': 'application/json',
  //     'Authorization': `Bearer ${localStorage.getItem("token")}`
  //   })
  //   // const requestData = { cart }; // Wrap cart data in an object
  //   const requestData = {
  //     cart: cart.map(item => ({
  //       price: item.price || 0,
  //       amount: item.amount || 0,
  //       desc: item.desc || "test"
  //     }))
  //   };
  //   console.log(requestData);
    
  //   return this.http.post<any>(this.SERVER_URL +"checkout",requestData, { headers: headers });
  // }

  login(pwd:string,user:string): Observable<any> {
    console.log({username:user,password:pwd});
    
    return this.http.post<any>(this.SERVER_URL +"login/",{username:user,password:pwd});
  }
}
