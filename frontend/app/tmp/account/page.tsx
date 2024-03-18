import GeneralButton from "@/components/common/GeneralButton";
import { IoChevronForwardOutline } from "react-icons/io5";
import styles from "@/styles/asdf.module.scss";
import Image from "next/image";

export default function Page() {
  return (
    <div className="w-[960px] py-24 px-10 mx-auto">
      <div className="uppercase mb-10 text-[28px] leading-none tracking-tight text-[#101010]">
        Your Account
      </div>
      <div className="p-10 bg-white flex justify-between">
        <div className="">
          <div className="mb-6 text-black text-[18px]">Available Balance</div>
          <div className="mb-1 text-black text-4xl">£0</div>
          <div className="text-[14px]">£0 Pending</div>
        </div>

        <div className="w-72 space-y-4">
          <GeneralButton lg action="black" title="sell items" />
          <GeneralButton lg action="white" title="WITHDRAWALS" />
        </div>
      </div>
      <div className="mt-8 bg-white text-[#101010]">
        <div className={styles.menu}>
          <div className={styles.menu_item}>
            <div className="w-[55px] h-[55px] mr-[14px]">
              <Image src="/icon-sneaker.svg" width={55} height={55} alt="asf" />
            </div>
            <div>
              <span className="font-bold">Selling</span>
              <p className="text-sm tracking-normal">
                You are currently selling 0 items
              </p>
            </div>
            <div className={styles.arrow}>
              <IoChevronForwardOutline size={16} />
            </div>
          </div>
          <div className={styles.menu_item}>
            <div className="w-[55px] h-[55px] mr-[14px]">
              <Image src="/icon-sneaker.svg" width={55} height={55} alt="asf" />
            </div>
            <div>
              <span className="font-bold">Orders</span>
              <p className="text-sm tracking-normal">
                View and edit your orders
              </p>
            </div>
            <div className={styles.arrow}>
              <IoChevronForwardOutline size={16} />
            </div>
          </div>
          <div className={styles.menu_item}>
            <div className="w-[55px] h-[55px] mr-[14px]">
              <Image src="/icon-sneaker.svg" width={55} height={55} alt="asf" />
            </div>
            <div>
              <span className="font-bold">Addresses</span>
              <p className="text-sm tracking-normal">
                Manage your delivery addresses
              </p>
            </div>
            <div className={styles.arrow}>
              <IoChevronForwardOutline size={16} />
            </div>
          </div>
          <div className={styles.menu_item}>
            <div className="w-[55px] h-[55px] mr-[14px]">
              <Image src="/icon-sneaker.svg" width={55} height={55} alt="asf" />
            </div>
            <div>
              <span className="font-bold">Account Details</span>
              <p className="text-sm tracking-normal">
                Manage your personal details
              </p>
            </div>
            <div className={styles.arrow}>
              <IoChevronForwardOutline size={16} />
            </div>
          </div>
          <div className={styles.menu_item}>
            <div className="w-[55px] h-[55px] mr-[14px]">
              <Image src="/icon-sneaker.svg" width={55} height={55} alt="asf" />
            </div>
            <div>
              <span className="font-bold">Stock Notifications</span>
              <p className="text-sm tracking-normal">
                Manage your email notifications
              </p>
            </div>
            <div className={styles.arrow}>
              <IoChevronForwardOutline size={16} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
