import BreadCrums from "../common/BreadCrums";
import GeneralButton from "../common/GeneralButton";

type Props = {
  button: boolean;
  title: string;
  breadCrum: string;
};

export default function Header({ button, title, breadCrum }: Props) {
  return (
    <div className="mb-4">
      <BreadCrums item={breadCrum} />
      <div className="pb-6 flex justify-between items-center">
        <h2 className="text-gray-950 uppercase text-[28px] leading-none tracking-tight">
          {title}
        </h2>
        {button && (
          <GeneralButton
            md
            action="black"
            title="sell items"
            style={{ paddingLeft: "32px", paddingRight: "32px" }}
          />
        )}
      </div>
    </div>
  );
}
