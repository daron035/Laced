import { createSlice } from "@reduxjs/toolkit";
import { create } from "domain";

interface ItemState {
  list: any;
}

const initialState = {
  list: [],
} as ItemState;

const sellItemsSlice = createSlice({
  name: "sellItems",
  initialState,
  reducers: {
    addSellItem: (state, { payload }) => {
      state.list.push(payload);
    },
  },
});

export const { addSellItem } = sellItemsSlice.actions;
export default sellItemsSlice.reducer;
