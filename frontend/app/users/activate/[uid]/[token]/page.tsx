"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import { useActivationMutation } from "@/redux/features/authApiSlice";
import toast from "react-hot-toast";

interface Props {
  params: {
    uid: string;
    token: string;
  };
}
export default function Page({ params }: Props) {
  const router = useRouter();
  const [activation] = useActivationMutation();

  useEffect(() => {
    const { uid, token } = params;
    let isApiSubscribed = true;

    activation({ uid, token })
      .unwrap()
      // .then((res) => {
      //   if (isApiSubscribed) {
      //     console.log("res", res);
      //     toast.success("Account activated");
      //   }
      // })
      .catch((e) => {
        if (isApiSubscribed) {
          console.log("catch", e.status);
          if (e.status === 403) {
            toast("Activated");
          } else {
            toast("Failed to activate account");
          }
        }
      })
      .finally(() => {
        router.push("/users/sign_in");
      });
    return () => {
      isApiSubscribed = false;
    };
  });

  return (
    <div className="flex min-h-full flex-1 flex-col justify-center px-6 pt-48 pb-80 lg:px-8">
      <div className="sm:mx-auto sm:w-full sm:max-w-sm">
        <h1 className="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">
          Activating your account...
        </h1>
      </div>
    </div>
  );
}
