export default function Form() {
  return (
    <form
      className="mb-[24px]"
      // onSubmit={(e) => onSubmit(e)}
    >
      <div className="mb-[24px]">
        <label
          className="text-xs text-[#777777] mb-[6px] "
          htmlFor="user_email"
        >
          First Name
        </label>
        <input
          className="bg-transparent border-[1px] border-[#ADAEAF] rounded
              w-full p-[14px] focus-visible:outline focus-visible:outline-[#101010]"
          type="text"
          name="username"
          id="First name"
          // onChange={(e) => onChange(e)}
          required
        />
      </div>

      <div>
        <input
          className="mr-[13px] accent-black outline-[#D0D0D0]"
          type="checkbox"
          id="check"
        />
        <label className="text-[#101010] text-sm" htmlFor="check">
          Remember Me
        </label>
      </div>
      <div className="my-[10px]">
        <input
          className="w-full bg-[#101010] text-white py-[16px] text-lg tracking-wider"
          type="submit"
          value="SIGN UP"
        />
      </div>
    </form>
  );
}
