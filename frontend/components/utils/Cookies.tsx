"use client";

import { GeneralButton, ToggleButton } from "@/components/common";
import { useEffect, useState } from "react";

export default function CookieModalView({ view }: { view: boolean }) {
  const [showCookie, setShowCookie] = useState(view);
  const [showPreferences, setShowPreferences] = useState(true);

  useEffect(() => {
    if (showCookie) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
    }
  }, [showCookie]);

  const closeCookie = () => {
    setShowCookie(false);
  };

  return (
    <div
      className={`z-10 fixed w-full h-screen text-black bg-black bg-opacity-50 ${showCookie ? "" : "hidden"}`}
    >
      <div className="m-10 p-8 bg-white absolute bottom-0 right-0 max-w-[38rem] text-sm tracking-tighter">
        {showPreferences ? (
          <div className="flex flex-col">
            <div className="text-2xl tracking-tight mb-4">
              COOKIES: THE BREAKDOWN
            </div>
            <div className="block pb-8 ">
              <div>
                <div className="flex justify-between items-center h-12">
                  <div>ESSENTIAL</div>
                  <div>Always Active</div>
                </div>
                <div>
                  Essential cookies are used for necessary functions like making
                  payments. These cookies can’t be switched off and they don’t
                  store any of your information.
                </div>
              </div>
              <div className="mt-8">
                <div className="flex justify-between items-center h-12">
                  <div>ANALYTICAL</div>
                  <div>
                    <ToggleButton id="analyticalToggle" />
                  </div>
                </div>
                <div>
                  Analytical cookies help us gather information to improve our
                  website and customer experience. They allow us to see things
                  like how many people are using our site and what pages are
                  popular. Switching off analytical cookies will mean we can’t
                  get that information.
                </div>
              </div>
              <div className="mt-8">
                <div className="flex justify-between items-center h-12">
                  <div>FUNCTIONAL</div>
                  <div>
                    <ToggleButton id="functionalToggle" />
                  </div>
                </div>
                <div>
                  Functional cookies are crucial for using certain elements of
                  Laced, like seeing ‘recently viewed’ products or searches.
                  Turning off these cookies means that some areas of our website
                  won’t work properly for you.
                </div>
              </div>
              <div className="mt-8">
                <div className="flex justify-between items-center h-12">
                  <div>ADVERTISING</div>
                  <div>Always Active</div>
                </div>
                <div>
                  Advertising cookies give us an insight into what products and
                  content you’re interested in. This allows us to show you
                  adverts on other websites that are completely tailored to you.
                  Turning off these cookies means we can’t show you personalised
                  adverts.
                </div>
              </div>
            </div>
            <div className="">
              <GeneralButton
                md
                action="black"
                title="save preferences"
                onClick={closeCookie}
              />
            </div>
          </div>
        ) : (
          <div className="grid grid-flow-col">
            <div className="pr-8 text-sm tracking-tight">
              <p>
                Laced uses cookies. Cookies are small files that are used to
                show you personalised content and improve your experience on our
                site. You can allow all cookies or manage them individually in
                your cookie settings.
              </p>
              <br />
              <p>
                Discover more via our{" "}
                <a href="#" style={{ textDecoration: "underline" }}>
                  cookie policy
                </a>
                .
              </p>
            </div>
            <div className="text-sm w-48 row-start-2 pl-8 mt-1 grid gap-7">
              <GeneralButton
                sm
                action="black"
                title="allow all"
                onClick={closeCookie}
              />
              <GeneralButton
                sm
                action="white"
                title="preferences"
                style={{
                  border: "none",
                  textDecoration: "underline",
                }}
                onClick={closeCookie}
              />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
