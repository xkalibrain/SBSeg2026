import { GrCircleInformation } from "react-icons/gr";

interface IHintElementProps{
    text: string
}

export default function HintElement({text}: IHintElementProps){
    return(
        <li className="flex flex-row w-full">
            <GrCircleInformation className="text-white mr-2 min-w-[25px]" size={25}/>
            <p className="w-fit">{text}</p>
        </li>
    );
}