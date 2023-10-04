"use client";

import { useSocialAuthenticateMutation } from "@/redux/features/authApiSlice";
import { useSocialAuth } from "@/hooks";

export default function Page() {
  const [vkAuthenticate] = useSocialAuthenticateMutation();
  useSocialAuth(vkAuthenticate, "vk-oauth2");

  return <div className="my-8">Loading...</div>;
}
