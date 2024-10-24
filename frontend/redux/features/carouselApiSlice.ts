import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

interface PreferencesProps {
  country: string;
  currency: string;
  country_iso: string;
  currency_iso: string;
}

export const GeneralAPI = createApi({
  reducerPath: "GeneralAPI",
  baseQuery: fetchBaseQuery({
    baseUrl: `${process.env.NEXT_PUBLIC_RTKQ}/api`,
    credentials: "include",
  }),
  tagTypes: ["Preferences"],
  endpoints: (build) => ({
    getPreferences: build.query<PreferencesProps, void>({
      query: () => ({
        url: `/preferences/`,
      }),
      providesTags: ["Preferences"],
    }),
  }),
});

export const { useGetPreferencesQuery } = GeneralAPI;
