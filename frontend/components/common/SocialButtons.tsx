"use client";

import { ImGoogle, ImVk } from "react-icons/im";
import { SocialButton } from "@/components/common";
import { continueWithGoogle, continueWithVk } from "@/utils";

export default function SocialButtons() {
  return (
    <div className="flex justify-between items-center gap-2 mb-[26px]">
      <SocialButton provider="google" onClick={continueWithGoogle}>
        <ImGoogle className="mr-3" /> Google Signin
      </SocialButton>
      <SocialButton provider="vk" onClick={continueWithVk}>
        <ImVk className="mr-3" /> Vk Signin
      </SocialButton>
    </div>
  );
}
