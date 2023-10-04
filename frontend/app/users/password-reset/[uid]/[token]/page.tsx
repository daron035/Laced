import { PasswordResetConfirmForm } from "@/components/forms";
import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Password Reset Confirm",
  description: "Password reset confirm page",
};

interface Props {
  params: {
    uid: string;
    token: string;
  };
}
export default function Page({ params: { uid, token } }: Props) {
  return (
    <div className="w-[560px] mx-auto px-[40px] pt-[80px] pb-[100px]">
      <h1 className="mb-[40px] text-[#101010] uppercase font-medium text-4xl subpixel-antialiased">
        RESET YOUR PASSWORD
      </h1>

      <PasswordResetConfirmForm uid={uid} token={token} />
    </div>
  );
}
