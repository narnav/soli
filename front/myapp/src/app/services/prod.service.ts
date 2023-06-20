import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProdService {
  constructor(private http: HttpClient) {}
  SERVER_URL = 'http://127.0.0.1:8000/prods';
  
  getProducts(): Observable<any> {
    return this.http.get<any>(this.SERVER_URL);
  }
  addProduct(prd: any): Observable<any> {
    return this.http.post<any>(this.SERVER_URL, prd);
  }
  delProduct(id: number): Observable<any> {
    return this.http.delete<any>(this.SERVER_URL + '/' + id);
  }
  updProduct(prd: any, id: number): Observable<any> {
    return this.http.put<any>(this.SERVER_URL + '/' + id, prd);
  }

  
}
