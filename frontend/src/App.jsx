import { useEffect, useState } from "react";
import API from "./services/api";

function App() {
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    try {
      const response = await API.get("/products");
      setProducts(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  return (
    <div>
      <h1>Product Management System</h1>

      {products.map((product) => (
        <div key={product.id}>
          <h3>{product.name}</h3>

          <p>ID: {product.id}</p>
          <p>Description: {product.disc}</p>
          <p>Price: ₹{product.price}</p>
          <p>Quantity: {product.quant}</p>

          <hr />
        </div>
      ))}
    </div>
  );
}

export default App;