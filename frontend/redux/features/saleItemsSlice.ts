import { createSlice } from "@reduxjs/toolkit";

interface ItemState {
  items: any;
}

const initialState = {
  items: null,
} as ItemState;

const saleItemsSlice = createSlice({
  name: "saleItems",
  initialState,
  reducers: {
    // addSaleItem: (state, { payload }) => {
    // addSaleItem: (state, { payload: PayloadAction<{ results: Item[] } }) => {
    // state.items = payload.results;
    // addSaleItem: (state, action: PayloadAction<{ results: Item[] }>) => {
    // state.items = action.payload.results;
    addSaleItem: (state, { payload }: PayloadAction<{ results: Item[] }>) => {
      state.items = payload.results;
    },
  },
});

export const { addSaleItem } = saleItemsSlice.actions;
export default saleItemsSlice.reducer;
