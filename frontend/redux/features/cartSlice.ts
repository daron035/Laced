import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";

// Асинхронное действие для добавления товара в корзину
export const addToCart = createAsyncThunk(
  "cart/addToCart",
  async ({ product_id, variation_id }, thunkAPI) => {
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_RTKQ}/api/cart/`, {
        method: "POST",
        body: JSON.stringify({
          product_id: product_id,
          variation_id: variation_id,
        }),
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
      });
      const data = await res.json();
      return { data, status: res.status };
      if (!res.ok) return undefined;
      return await res.json();
    } catch (err) {
      console.log(err);
      return thunkAPI.rejectWithValue(err);
    }
  },
);
// Асинхронное действие для добавления товара в корзину
export const removeFromCart = createAsyncThunk(
  "cart/removeFromCart",
  async ({ product_id, variation_id, price }, thunkAPI) => {
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_RTKQ}/api/cart/`, {
        method: "DELETE",
        body: JSON.stringify({
          product_id: product_id,
          variation_id: variation_id,
        }),
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
      });
      // const data = await res.json();
      // return { data, status: res.status };
      if (!res.ok) return undefined;
      return await res.json();
      const i = await res.json();
      return { i, price };
      // if (res.ok) {
      //   return { product_id, variation_id, status: res.status };
      // } else {
      //   return thunkAPI.rejectWithValue(await res.json());
      // }
      return 35;
    } catch (err) {
      console.log(err);
      return thunkAPI.rejectWithValue(err);
    }
  },
);

// Асинхронное действие для получения корзины
export const fetchCart = createAsyncThunk(
  "cart/fetchCart",
  async (_, thunkAPI) => {
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_RTKQ}/api/cart/`, {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
      });
      if (!res.ok) return undefined;
      // return await res.json();
      const data = await res.json();
      return data;
    } catch (err) {
      console.log(err);
      return thunkAPI.rejectWithValue(err);
    }
  },
);

interface CartItem {
  id: number;
  product_id: number;
  name: string;
  image: string;
  variation: string;
  price: {
    symbol: string;
    currency: string;
    value: string;
  };
  variation_id: number;
}

interface CartState {
  items: CartItem[];
  count: number;
  currency: string;
  subtotal: any;
  status: "idle" | "pending" | "succeeded" | "failed";
  error: string | undefined;
}

const initialState = {
  items: [],
  count: 0,
  currency: "",
  subtotal: "",
  status: "idle",
  error: undefined,
} as CartState;

const cartSlice = createSlice({
  name: "cart",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      // Обработка состояний для fetchCart
      .addCase(fetchCart.pending, (state) => {
        state.status = "pending";
      })
      .addCase(fetchCart.fulfilled, (state, action) => {
        state.status = "succeeded";
        state.items = action.payload.data || []; // Здесь изменяем items
        state.subtotal = action.payload.cart_total_price;
        state.count = action.payload.count || 0;
      })
      .addCase(fetchCart.rejected, (state, action) => {
        state.status = "failed";
        state.error = action.error.message;
      })
      // Обработка состояний для addToCart
      .addCase(addToCart.pending, (state) => {
        state.status = "pending";
      })
      .addCase(addToCart.fulfilled, (state, action) => {
        state.status = "succeeded";
        if (action.payload.status === 200) {
          state.items.push(action.payload.data);
          state.count += 1;
        }
      })
      .addCase(addToCart.rejected, (state, action) => {
        state.status = "failed";
        state.error = action.error.message;
      })
      // Обработка состояний для removeFromCart
      .addCase(removeFromCart.pending, (state) => {
        state.status = "pending";
      })
      .addCase(removeFromCart.fulfilled, (state, action) => {
        console.log("32322332233223", action.meta.arg.price);
        state.items = state.items.filter((item) => item.id !== action.payload);
        // console.log("👍", Number(state.subtotal));
        console.log("👍", Number(action.meta.arg.price));
        let a = String(Number(state.subtotal) - Number(action.meta.arg.price));
        state.subtotal = a; // console.log("👍", state.subtotal);
        state.count -= 1;
        // state.items = state.items.filter((item) => item.id !== 35);
      })
      .addCase(removeFromCart.rejected, (state, action) => {
        state.status = "failed";
        state.error = action.error.message;
      });
  },
});

export const cartReducer = cartSlice.reducer;
