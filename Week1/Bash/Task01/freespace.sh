#!/bin/bash

#Name:Raziel Afandaev





#Defaults
prefix="fc-"
flag=true
timeout=48
recursive=0

#
while getopts ":rt:" opt; do
  case $opt in
    r) recursive=1;; #Traverse mode
    t) timeout=$OPTARG;; #Set timeout
    \?) echo "Invalid option: -$OPTARG">&2;;
  esac  
done

shift $((OPTIND-1))


#compress file 
compressFiles(){
  dir=$(dirname "$@")
  filename=$(basename $@)
  outname="$prefix"${filename%%.*}
  if [[ "${filename%%-*}-" == "$prefix" ]]; then
      touch -m -a ${filename}
  else
    filetype=$(file -b "$@" | awk '{print tolower($1)}')
    case  $filetype in #if alredy compressed rename and update timestamp
      bzip2 | zip | compress* | gzip) mv $@ ${prefix}${filename}  && touch -a -m ${prefix}${filename}  ;;
      *) tar -czf $dir/$outname.tar $dir/$filename;;
    esac
  fi

}



deleteFiles() {
  lifespan=$((60*timeout-1 ))   #lifespan of the file less than 47.59H  in minutes
  if [[ $recursive -eq 1 ]]; then
      find $(dirname $@) -type f -name "fc-*" -mmin +$lifespan -exec rm {} \;
  else
      find $(dirname $@) -maxdepth 1 -type f  -name "fc-*" -mmin +$lifespan -exec rm {} \;

  fi

}
#free space of given file compress and delete
freeFiles(){
deleteFiles $@
compressFiles $@
}



freeDir(){
	
	for arg in "$@" ; do
		if [[ $recursive -eq 1 ]] ; then
			if [[ -d $arg ]] ; then
				freeDir "${arg}"/*
			elif [[ -f $arg ]]; then
        
				freeFiles ${arg}
			fi
		elif [[  $recursive -eq 0 ]]; then
				if [[ -d $arg ]] && $flag; then
					flag=false
					freeDir "${arg}"/*
			elif [[ -f $arg ]]; then
        
				freeFiles ${arg}
			fi
        fi
	done

}


freeDir $@