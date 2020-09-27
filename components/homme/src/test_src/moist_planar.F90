
#ifndef CAM
#include "config.h"

module moist_planar_tests

  use element_mod,          only: element_t
  use hybrid_mod,           only: hybrid_t
  use hybvcoord_mod,        only: hvcoord_t
  use parallel_mod,         only: abortmp

  implicit none
  contains

  ! planar moist density current
  subroutine mdc_init(elem,hybrid,hvcoord,nets,nete)


    type(element_t),    intent(inout), target :: elem(:)                  ! element array
    type(hybrid_t),     intent(in)            :: hybrid                   ! hybrid parallel structure
    type(hvcoord_t),    intent(inout)         :: hvcoord                  ! hybrid vertical coordinates
    integer,            intent(in)            :: nets,nete                ! start, end element index

    call abortmp('planar moist density current not yet implemented')

  end subroutine mdc_init

  ! planar moist rising bubble
  subroutine mrb_init(elem,hybrid,hvcoord,nets,nete)


    type(element_t),    intent(inout), target :: elem(:)                  ! element array
    type(hybrid_t),     intent(in)            :: hybrid                   ! hybrid parallel structure
    type(hvcoord_t),    intent(inout)         :: hvcoord                  ! hybrid vertical coordinates
    integer,            intent(in)            :: nets,nete                ! start, end element index

    call abortmp('planar moist rising bubble not yet implemented')

  end subroutine mrb_init


  ! planar moist baroclinic instability
  subroutine mbi_init(elem,hybrid,hvcoord,nets,nete)


    type(element_t),    intent(inout), target :: elem(:)                  ! element array
    type(hybrid_t),     intent(in)            :: hybrid                   ! hybrid parallel structure
    type(hvcoord_t),    intent(inout)         :: hvcoord                  ! hybrid vertical coordinates
    integer,            intent(in)            :: nets,nete                ! start, end element index

    call abortmp('planar moist baroclinic instability not yet implemented')

  end subroutine mbi_init

  ! planar tropical cyclone
  subroutine tc_init(elem,hybrid,hvcoord,nets,nete)


    type(element_t),    intent(inout), target :: elem(:)                  ! element array
    type(hybrid_t),     intent(in)            :: hybrid                   ! hybrid parallel structure
    type(hvcoord_t),    intent(inout)         :: hvcoord                  ! hybrid vertical coordinates
    integer,            intent(in)            :: nets,nete                ! start, end element index

    call abortmp('planar tropical cyclone not yet implemented')

  end subroutine tc_init

  ! planar supercell
  subroutine sc_init(elem,hybrid,hvcoord,nets,nete)


    type(element_t),    intent(inout), target :: elem(:)                  ! element array
    type(hybrid_t),     intent(in)            :: hybrid                   ! hybrid parallel structure
    type(hvcoord_t),    intent(inout)         :: hvcoord                  ! hybrid vertical coordinates
    integer,            intent(in)            :: nets,nete                ! start, end element index

    call abortmp('planar supercell not yet implemented')

  end subroutine sc_init


end module moist_planar_tests
#endif
