"use client";

import { useState } from "react";

export default function ToggleButton({ id }: { id: string }) {
  const [isChecked, setIsChecked] = useState(true);

  const handleToggle = () => {
    setIsChecked(!isChecked);
  };

  return (
    <div className="flex items-center justify-center w-full select-none">
      <label htmlFor={id} className="flex items-center cursor-pointer">
        <div className="mr-3 text-gray-700 font-medium">
          {isChecked ? "Active" : "Inactive"}
        </div>
        {/* toggle */}
        <div className="relative">
          {/* input */}
          <input
            id={id}
            type="checkbox"
            className="sr-only"
            checked={isChecked}
            onChange={handleToggle}
          />
          {/* line */}
          <div
            className={`w-12 h-4 rounded-full shadow-inner transition ${
              isChecked ? "bg-green-200" : "bg-gray-300"
            }`}
          ></div>
          {/* dot */}
          <div
            className={`dot absolute w-6 h-6 bg-white rounded-full shadow -left-0 -top-1 transition ${
              isChecked ? "bg-green-500 translate-x-full" : ""
            }`}
          ></div>
        </div>
      </label>
    </div>
  );
}
