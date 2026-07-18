import { Section } from "@/app/result/page"

type SectionButtonProps = {
    section: Section
    onSelect: (section: Section) => void
    isCurrent: boolean
}

export default function SectionButton({ section, onSelect, isCurrent }: SectionButtonProps){
    return (
        <button
            className={
                "p-5 text-white rounded-md border border-blue-kali grow"
                + (isCurrent ? " bg-blue-kali" : " bg-slate-kali")
            }
            onClick={() => onSelect(section)}
        >
            {section.title}
        </button>
    )
}
