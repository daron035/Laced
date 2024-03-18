"use client";

import { IoAddOutline, IoRemoveOutline } from "react-icons/io5";
import { useRef, useState } from "react";
import Image from "next/image";

export const faqs = [
  {
    question: "Authenticated",
    answer:
      "Tenetur ullam rerum ad iusto possimus sequi mollitia dolore sunt quam praesentium. Tenetur ullam rerum ad iusto possimus sequi mollitia dolore sunt quam praesentium.Tenetur ullam rerum ad iusto possimus sequi mollitia dolore sunt quam praesentium.",
  },
  {
    question: "Brand new & unused",
    answer:
      "Aperiam ab atque incidunt dolores ullam est, earum ipsa recusandae velit cumque. Aperiam ab atque incidunt dolores ullam est, earum ipsa recusandae velit cumque.",
  },
  {
    question: "Quick delivery",
    answer:
      "Blanditiis aliquid adipisci quisquam reiciendis voluptates itaque.",
  },
];

const AccordionItem = ({ faq, active, onToggle }: any) => {
  const { question, answer } = faq;

  const contentEl = useRef<HTMLDivElement | null>(null);

  return (
    <div className="overflow-hidden text-gray-950">
      <button
        className="px-3 py-4 border-b w-full flex items-center gap-x-2"
        onClick={onToggle}
      >
        <Image src="/12.svg" width={48} height={48} alt="asf" />
        <span className="uppercase ">{question}</span>
        <span className="ml-auto">
          {active ? <IoRemoveOutline size={26} /> : <IoAddOutline size={26} />}
        </span>
      </button>
      <div
        ref={contentEl}
        className={`h-0 duration-200 ease-in-out`}
        style={
          active
            ? { height: `${contentEl.current.scrollHeight}px` }
            : { height: "0px" }
        }
      >
        <div className="pt-6 pr-8 pb-6 pl-6 leading-normal">{answer}</div>
      </div>
    </div>
  );
};

export default function Accordion() {
  const [clicked, setClicked] = useState<any>("0");

  const handleToggle = (index: any) => {
    console.log(index);
    if (clicked === index) {
      return setClicked("0");
    }
    setClicked(index);
  };

  return (
    <div className="py-8 border-t">
      {faqs.map((faq, index) => (
        <AccordionItem
          onToggle={() => handleToggle(index)}
          active={clicked === index}
          key={index}
          faq={faq}
        />
      ))}
    </div>
  );
}
