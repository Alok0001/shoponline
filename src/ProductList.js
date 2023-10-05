import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'; 

const ProductList = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios
      .get('http://localhost:5000/products')
      .then((response) => {
        setProducts(response.data);
      })
      .catch((error) => {
        console.error('Error fetching products:', error);
      });
  }, []);

  return (
    <div className="container">
      <h2 className="mt-5">Product List</h2>
      <div className="row">
        {products.map((product) => (
          <div key={product._id} className="col-lg-6 col-md-6 col-sm-12 mb-4">
            <div className="card">
              <img
                src={product.image}
                className="card-img-top"
                alt={product.title}
              />
              <div className="card-body">
                <h5 className="card-title">{product.title}</h5>
                <p className="card-text">Price: ${product.price}</p>
                <p className="card-text">Category: {product.category}</p>
                <p className="card-text">{product.description}</p>
              </div>
              <div className="card-footer">
                <button className="btn btn-primary btn-sm">Add to Cart</button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ProductList;
