'use client'
import Image from "next/image"
import { IoMdSearch } from "react-icons/io"
import { useRouter } from 'next/navigation'
import { MdArrowDropDown, MdArrowDropUp } from "react-icons/md"
import { useState } from "react"
import { CustomButton } from "@/app/components/customButton"

export default function HomePage(){
    const router = useRouter()
    const [isOpen, setIsOpen] = useState(false)
    const [optionSelected, setOptionSelected] = useState("https")
    const [inputValue, setInputValue] = useState("")

    const options = ["https", "http"]

    const listElements = options.map((value) => <li key={value}>
        <button
            onClick={() => {
                setOptionSelected(value)
            }}
            className={`pl-5 pr-5 pb-2 pt-2 flex items-center ${value == optionSelected ? 'text-blue-500' : 'text-black'}`}
            type="button"
        >
            {value}
        </button>
    </li>)

    return (
        <div className="self-center flex flex-col items-center">
            <Image
                src="/xkaliburr_logo.svg"
                alt="logo"
                width={250}
                height={24}
                priority
            />
            <form
                className="flex flex-col items-center justify-center text-sm pt-10 gap-2"
                onSubmit={(e) => {
                    e.preventDefault()
                    router.push(`/result?option=${optionSelected}&search=${inputValue}`)
                }}
            >
                <div className="flex flex-row gap-3 border border-white rounded-md bg-slate-600 p-3 mb-5 w-full">
                    <button
                        type='button'
                        className="px-1 flex flex-row justify-between text-blue-500 w-[80px] relative"
                        onClick={() => setIsOpen(!isOpen)}
                    >
                        <p>{optionSelected}</p>
                        {isOpen ? <MdArrowDropUp size={23}/> : <MdArrowDropDown size={23}/>}
                        <ul className={`
                            ${isOpen || "hidden"} absolute h-fit w-fit bg-white border rounded-md p-3
                            bottom-0 translate-y-28 left-0 -translate-x-3
                        `}>
                            {listElements}
                        </ul>
                    </button>
                    <div className="border-l-2"></div>
                    <IoMdSearch className="text-blue-500 min-w-[20px]" size={20} />
                    <input
                        className="text-gray-400 bg-slate-600 w-64"
                        placeholder="Insira a URL que você deseja escanear"
                        value={inputValue}
                        onChange={(e) => { setInputValue(e.target.value) }}
                    >
                    </input>
                </div>
                <CustomButton
                    type="submit"
                    text="REALIZAR ANÁLISE"
                />
            </form>
        </div>
    )
}
