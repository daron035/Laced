import Actions from "../product/Actions";
import Accordion from "../product/Accordion";
import Details from "./Details";
import Header from "../product/Header";

import { Size } from "@/utils/countries.utils";

type Props = {
  data: Size[];
};

export default function Info({ data }: Props) {
  return (
    <div className="shrink-0 w-[420px] pt-[32px]">
      <Header
        brand={"AIR JORDAN"}
        sku={"DH6927-161"}
        name={"AIR JORDAN 4 RETRO RED CEMENT"}
      />
      <Actions data={data} />
      <Accordion />
      <Details />
    </div>
  );
}
