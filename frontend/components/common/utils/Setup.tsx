"use client";

import { useVerify } from "@/hooks";
import { Toaster } from "react-hot-toast";

export default function Setup() {
  useVerify();

  return (
    <Toaster
      position="top-right"
      containerStyle={{ marginTop: "72px" }}
      reverseOrder={false}
      toastOptions={{ duration: 5000 }}
    />
  );
}
