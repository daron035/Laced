import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const GeneralAPI = createApi({
  reducerPath: "GeneralAPI",
  baseQuery: fetchBaseQuery({
    baseUrl: `${process.env.NEXT_PUBLIC_HOST}/api`,
    credentials: "include",
  }),
  tagTypes: ["Preferences"],
  endpoints: (build) => ({
    getPreferences: build.query<{ country: string; currency: string }, void>({
      query: () => ({
        url: `/preferences/`,
      }),
      providesTags: ["Preferences"],
    }),
  }),
});

export const { useGetPreferencesQuery } = GeneralAPI;
