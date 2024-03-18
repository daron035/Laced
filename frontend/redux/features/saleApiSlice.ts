import { apiSlice } from "../services/apiSlice";

interface User {
  first_name: string;
  last_name: string;
  email: string;
}

interface SocialAuthArgs {
  provider: string;
  state: string;
  code: string;
}

interface CreateUserResponse {
  success: boolean;
  user: User;
}

const saleApiSlice = apiSlice.injectEndpoints({
  endpoints: (builder) => ({
    retrieveSaleItems: builder.query<any[], { style_codes: string | null }>({
      query: ({ style_codes }) => ({
        url: `/product`,
        // /add-product-list?style_codes={SKU}
        params: {
          style_codes,
        },
      }),
    }),
    test: builder.query<any, void>({
      query: () => "/product",
    }),
  }),
});

export const { useRetrieveSaleItemsQuery, useTestQuery } = saleApiSlice;
