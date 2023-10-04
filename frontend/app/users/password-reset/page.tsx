import { PasswordResetForm } from "@/components/forms";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Password Reset",
  description: "Password reset page",
};

export default function Page() {
  return (
    <div className="w-[560px] mx-auto px-[40px] pt-[80px] pb-[100px]">
      <h1 className="mb-[40px] text-[#101010] uppercase font-medium text-4xl subpixel-antialiased">
        CHANGE YOUR PASSWORD
      </h1>

      <PasswordResetForm />
    </div>
  );
}
