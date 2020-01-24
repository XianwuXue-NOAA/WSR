set -xe  # print commands as they are executed and enable signal trapping

export PS4='+ $SECONDS + ' 

# Variables needed for communication with ecFlow
  if (( 0 == 1 )); then
export ECF_NAME=%ECF_NAME%
#export ECF_HOST=%ECF_HOST%
export ECF_HOST=%ECF_LOGHOST%
export ECF_PORT=%ECF_PORT%
export ECF_PASS=%ECF_PASS%
export ECF_TRYNO=%ECF_TRYNO%
export ECF_RID=$LSB_JOBID
  fi

# Tell ecFlow we have started
# POST_OUT variable enables LSF post_exec to communicate with ecFlow
if [ -d /opt/modules ]; then
    # WCOSS TO4 (Cray XC40)
    echo "WCOSS TO4 (Cray XC40)"
    . /opt/modules/default/init/sh
    # module load ecflow
    # POST_OUT=/gpfs/hps/tmpfs/ecflow/ecflow_post_in.$LSB_BATCH_JID
elif [ -d /usrx/local/Modules ]; then
    # WCOSS Phase 1 & 2 (IBM iDataPlex)
    echo "WCOSS Phase 1 & 2 (IBM iDataPlex)"
    . /usrx/local/Modules/default/init/sh
    # module load ecflow
    # POST_OUT=/var/lsf/ecflow_post_in.$LSB_BATCH_JID
else
    # WCOSS Phase 3 (Dell PowerEdge)
    echo " WCOSS Phase 3 (Dell PowerEdge)"
    . /usrx/local/prod/lmod/lmod/init/sh
    #module load ips/18.0.1.163 ecflow/%ECF_VERSION%
    module load ips/18.0.1.163
    # POST_OUT=/var/lsf/ecflow_post_in.$USER.$LSB_BATCH_JID
fi
  if (( 0 == 1 )); then
ecflow_client --init=${ECF_RID}

cat > $POST_OUT <<ENDFILE
ECF_NAME=${ECF_NAME}
ECF_HOST=${ECF_HOST}
ECF_PORT=${ECF_PORT}
ECF_PASS=${ECF_PASS}
ECF_TRYNO=${ECF_TRYNO}
ECF_RID=${ECF_RID}
ENDFILE
  fi

# Define error handler
ERROR() {
  set +ex
  if [ "$1" -eq 0 ]; then
     msg="Killed by signal (likely via bkill)"
  else
     msg="Killed by signal $1"
  fi
  # ecflow_client --abort="$msg"
  echo $msg
  # echo "Trap Caught" >>$POST_OUT
  trap $1; exit $1
}
# Trap all error and exit signals
trap 'ERROR $?' ERR EXIT

