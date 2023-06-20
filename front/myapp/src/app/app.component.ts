import { Component } from '@angular/core';
import { AuthService } from './services/auth.service';
import { ProdService } from './services/prod.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'myapp';
  myProducts: any[] = []
  cart:any[]=[]
  constructor(private prodSrv: ProdService, private auth: AuthService) {

    this.getData()
  }
  buy(price: number, desc: string, id: number) {
    
    this.cart.push({amount:1,desc,price})
    console.log( this.cart);
  }
  getData() {
    this.prodSrv.getProducts().subscribe(res => this.myProducts = res)
  }
  add(price: number, desc: any) {
    this.prodSrv.addProduct({ price, desc }).subscribe(res => console.log(res))
    this.getData()
  }
  del(id: number) {
    this.prodSrv.delProduct(id).subscribe(res => console.log(res))
    this.getData()
  }

  upd(price: number, desc: string, id: number) {
    this.prodSrv.updProduct({ price, desc }, id).subscribe(res => console.log(res))
    this.getData()
  }
  checkOut() {
    this.auth.checkOut(this.cart).subscribe(res => console.log(res))
  }
  login(pwd: string, user: string) {
    this.auth.login(pwd, user).subscribe(res => localStorage.setItem("token", res.access))
  }
}
