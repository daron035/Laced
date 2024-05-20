"use client";

import { useEffect, useState } from "react";

// import PreferencesModal from "@/components/PreferencesModal";

import { useRetrievePreferencesQuery } from "@/redux/features/carouselApiSlice";

export default function Footer() {
  // const { data, error, isLoading, isSuccess, refetch } =
  //   useRetrievePreferencesQuery();

  const [preferences, setPreferences] = useState({
    country: null,
    currency: null,
  });
  // useEffect(() => {
  //   if (isSuccess && data) {
  //     setPreferences({
  //       ...preferences,
  //       country: data.country_name,
  //       currency: data.currency_iso,
  //     });
  //   }
  // }, [isSuccess, data]);

  const [viewModal, setModal] = useState(false);

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
      {/* <PreferencesModal */}
      {/*   display={viewModal} */}
      {/*   pref={preferences} */}
      {/*   callbackClose={callbackCloseModal} */}
      {/* /> */}
      <h1 className="bg-gray-950 h-16 select-none outline-none">
        <div className="h-full px-2">
          <div className="flex items-center justify-center h-full">
            {/* <button */}
            {/*   className="text-white px-4 py-2 border border-[#343536] hover:bg-gray-100 hover:text-black duration-200" */}
            {/*   onClick={() => openModal()} */}
            {/* > */}
            {/*   <span>{isSuccess && data.country_name}</span> */}
            {/*   <span className="px-1 text-sm font-bold">|</span> */}
            {/* <span>{isSuccess && data.currency_iso}</span> */}
            {/*   <span>лангуаге</span> */}
            {/*   <span className="px-1 text-sm font-bold">|</span> */}
            {/*   <span> */}
            {/*     {isSuccess && `${data.currency_symbol} ${data.currency_iso}`} */}
            {/*   </span> */}
            {/* </button> */}
            <p className="text-[#FAF9F8] text-xs">
              &copy; 2023 Laced, Inc. All Rights Reserved.
            </p>
          </div>
        </div>
      </h1>
    </nav>
  );
}
