"use client";

import { useEffect, useState } from "react";
import PreferencesModal from "@/components/PreferencesModal";
import { useGetPreferencesQuery } from "@/redux/features/carouselApiSlice";

interface PreferencesProps {
  country: string | null;
  currency: string | null;
  country_iso: string | null;
  currency_iso: string | null;
}

export default function Footer() {
  const { data, error, isLoading, isSuccess } = useGetPreferencesQuery();

  const [preferences, setPreferences] = useState<PreferencesProps>({
    country: null,
    currency: null,
    country_iso: null,
    currency_iso: null,
  });

  useEffect(() => {
    if (isSuccess && data) {
      setPreferences({
        country: data.country,
        currency: data.currency,
        country_iso: data.country_iso,
        currency_iso: data.currency_iso,
      });
    }
  }, [isSuccess, data]);

  const [viewModal, setModal] = useState<boolean>(false);

  function openModal() {
    setModal(true);
    document.body.style.overflow = "hidden";
  }

  function callbackCloseModal() {
    setModal(false);
    document.body.style.overflow = "";
  }

  return (
    <nav>
      {viewModal && (
        <PreferencesModal
          preferences={preferences}
          callbackClose={callbackCloseModal}
        />
      )}
      <h1 className="bg-gray-950 h-16 select-none outline-none">
        <div className="h-full px-2">
          <div className="flex items-center justify-center h-full">
            {isSuccess && (
              <button
                className="text-white px-4 py-2 border border-[#343536] hover:bg-gray-100 hover:text-black duration-200"
                onClick={() => openModal()}
              >
                <span>{data.country}</span>
                <span className="px-1 text-sm font-bold">|</span>
                <span>English</span>
                <span className="px-1 text-sm font-bold">|</span>
                <span>{data.currency}</span>
              </button>
            )}
            <p className="text-[#FAF9F8] text-xs">
              &copy; 2023 Laced, Inc. All Rights Reserved.
            </p>
          </div>
        </div>
      </h1>
    </nav>
  );
}
